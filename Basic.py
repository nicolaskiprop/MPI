from mpi4py import MPI

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

if rank != 0:
    message='Hello from '+str(rank)
    comm.send(message, dest=0)
else:
    for procid in range(1, size):
        message=comm.recv(source= procid)
    print("Process 0 recieves message from process", procid, ":" , message)

