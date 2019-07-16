import transaction_pb2
import transaction_pb2_grpc
import grpc
from concurrent import futures
import time
import datetime
import uuid

class TransactionServicer(transaction_pb2_grpc.TransactionServicer):
    def newTransaction(self, request, context):
        print("got new transaction from user " + request.phone_number)
        payload = {
            "status": "1",
            "biller_message": uuid.uuid4().hex,
            "created_at": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "update_at": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            }
        response = transaction_pb2.TransactionResponse(**payload)
        return response

_ONE_DAY_IN_SECONDS = 60 * 60 * 24    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    transaction_pb2_grpc.add_TransactionServicer_to_server(TransactionServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()