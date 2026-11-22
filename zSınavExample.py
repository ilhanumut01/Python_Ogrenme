from mpi4py import MPI # MPI kütüphanesini içe aktar
comm = MPI.COMM_WORLD  # MPI iletişim dünyasını başlat
rank = comm.Get_rank()  # Prosesin kimlik numarasını al
size = comm.Get_size()  # Toplam proses sayısını al
print(f"hello World, process id: {rank} of {size}")  # Her proses kendi kimliğini ve toplam proses sayısını yazdır
MPI.Finalize()  # MPI evrenini sonlandır