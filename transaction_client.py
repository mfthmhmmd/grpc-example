import transaction_pb2
import transaction_pb2_grpc
import grpc

channel = grpc.insecure_channel('localhost:50051')
stub = transaction_pb2_grpc.TransactionStub(channel)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = transaction_pb2_grpc.TransactionStub(channel)
        
        transaction_request = transaction_pb2.TransactionRequest(
            phone_number="0822223344",
            customer_number="0811223344",
            amount = 1,
        )
        r = stub.newTransaction(transaction_request)
        print(r)

if __name__ == "__main__":
    run()