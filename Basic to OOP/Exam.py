import serial
import time
from datetime import datetime

# ---------------------------------------------------------
# FRAME FORMATTING FUNCTION (FRAME GENERATOR)
# ---------------------------------------------------------
def genFrame(PD=[]):
    """
    Generates the data frame structure for the NFC/RFID reader (e.g., PN532).
    Automatically calculates the required length and checksum (DCS).
    """
    f = [0x00, 0x00, 0xff]                 # Standard frame preamble
    f.append(len(PD) + 1)                  # LEN: Data length + 1
    f.append((256 - (len(PD) + 1)) % 256)  # LCS: Length checksum
    f.append(0xD4)                         # Direction identifier (Host to Reader)
    f.extend(PD)                           # Payload data (Command injection)
    
    # Data Checksum (DCS) calculation
    dcs = 0xD4
    for i in range(0, len(PD)):
        dcs = dcs + PD[i]
        
    f.append((256 - (dcs & 0xff)) % 256)   # DCS Checksum
    f.append(0x00)                         # Frame postamble
    return f

# ---------------------------------------------------------
# DATA RECEPTION FUNCTION (SERIAL READ)
# ---------------------------------------------------------
def read_from_reader(ser, delay=0.1):
    """
    Waits for a specified time and reads the accumulated data in the serial port.
    """
    time.sleep(delay)
    c = ser.inWaiting() # Checks if there are bytes available in the buffer
    if c:
        return ser.read(c)
    return None

def main():
    # Serial connection configuration with the reader
    try:
        ser = serial.Serial("COM3", 115200, 8, 'N', 1)
        print("System: Successful connection on port COM9.")
    except Exception as e:
        print(f"System: Connection error -> {e}")
        return

    # Hardware initialization phase
    print("System: Waking up the reader (Wake-up)...")
    ser.write(bytes([0x55, 0x55, 0x00, 0x00, 0x00]))
    time.sleep(0.002)

    print("System: Configuring reader parameters...")
    ser.write(bytes(genFrame([0x14, 0x01, 0x14, 0x01])))
    read_from_reader(ser, 0.1)

    print("\n[+] Waiting for a card... (Press Ctrl+C to stop the program)")
    
    try:
        while True:
            # Command to detect cards (InListPassiveTarget)
            ser.write(bytes(genFrame([0x4a, 0x01, 0x00])))
            
            # --- FAST SCAN MODIFICATION ---
            # We reduce the wait time to ~22ms (0.02s) following the professor's instructions.
            # This optimizes the loop: if no card is present on the reader,
            # the program doesn't freeze waiting and restarts the loop immediately.
            r = read_from_reader(ser, 0.02) 

            if r:
                # Search for the reader's response signature (0xD5 0x4B)
                idx = r.find(b'\xd5\x4b')
                
                # If the signature is found AND the number of detected cards is greater than 0
                if idx != -1 and r[idx + 2] > 0:
                    print("\n------------------------------------------------")
                    
                    # Extraction of the card's Unique Identifier (UID)
                    uid_length = r[idx + 7]
                    uid = r[idx + 8 : idx + 8 + uid_length]
                    uid_formatted = ':'.join([f"{b:02X}" for b in uid])
                    print(f"-> *** CARD DETECTED | UID: {uid_formatted} ***")

                    # Authentication of Block 1 using default Key A
                    tx = [0x40, 0x01, 0x60, 0x01] # MIFARE authentication command
                    tx.extend([0xff, 0xff, 0xff, 0xff, 0xff, 0xff]) # Standard Key A (FF FF FF FF FF FF)
                    tx.extend(uid) # The UID is included for the pairing process

                    ser.write(bytes(genFrame(tx)))
                    auth_r = read_from_reader(ser, 0.1)

                    # If authentication is successful (Confirmation signature: 0xD5 0x41 0x00)
                    if auth_r and b'\xd5\x41\x00' in auth_r:
                        
                        # 1. READ EXISTING DATA IN BLOCK 1
                        tx_read = [0x40, 0x01, 0x30, 0x01] # Block 1 read command
                        ser.write(bytes(genFrame(tx_read)))
                        read_r = read_from_reader(ser, 0.1)
                        
                        if read_r:
                            read_idx = read_r.find(b'\xd5\x41\x00')
                            if read_idx != -1 and len(read_r) >= read_idx + 3 + 16:
                                # Extract the 16 bytes corresponding to the memory block
                                block_data = read_r[read_idx + 3 : read_idx + 3 + 16]
                                hex_data = ' '.join([f"{b:02X}" for b in block_data])
                                ascii_data = ''.join([chr(b) if 32 <= b <= 126 else '.' for b in block_data])
                                
                                print(f"-> [READ] Hex   : {hex_data}")
                                print(f"-> [READ] ASCII : {ascii_data}")

                        # 2. WRITE NEW DYNAMIC DATA (CURRENT TIME) TO BLOCK 1
                        current_time = datetime.now().strftime("%H:%M:%S")
                        payload_text = f"TIME {current_time}"
                        payload_text = payload_text.ljust(16, ' ') # Pad with spaces until the mandatory 16 bytes are completed
                        payload_bytes = [ord(c) for c in payload_text] # Convert ASCII characters to bytes
                        
                        tx_write = [0x40, 0x01, 0xA0, 0x01] # Block 1 write command
                        tx_write.extend(payload_bytes)

                        ser.write(bytes(genFrame(tx_write)))
                        write_r = read_from_reader(ser, 0.1)

                        if write_r and b'\xd5\x41\x00' in write_r:
                            print(f"-> [WRITE] Success! Wrote: '{payload_text}'")
                        else:
                            print("-> [WRITE] Error writing to the card.")
                    else:
                        print("-> Authentication Error! Incorrect key.")
                        
                    print("------------------------------------------------")
                    
                    # --- SMART COOLDOWN MODIFICATION ---
                    # Once reading and writing are finished, we pause the program for 1.5 seconds.
                    # This prevents an aggressive infinite loop from reading/writing to the same card 50 times per second.
                    time.sleep(1.5)
                    
                    # CRITICAL NOTE: During this 1.5-second pause, it is very likely the user
                    # has left the card resting on the reader. This generates repeated "garbage" data
                    # in the serial buffer. With the following line, we clear the input buffer before restarting
                    # the loop to guarantee a clean read in the next iteration.
                    ser.reset_input_buffer()

    except KeyboardInterrupt:
        print("\nSystem: Terminating the program safely...")
        ser.close()

if __name__ == "__main__":
    main()