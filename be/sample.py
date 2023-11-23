from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials


def main():
    JSON_PATH = 'todo-app-88565-firebase-adminsdk-z4fsl-e2a8f69d03.json'
    # Firebase初期化
    cred = credentials.Certificate(JSON_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc = db.collection('tasks')
    doc.add({'task': "ddd"})

def main2():
    #データベース内を表示
    JSON_PATH = 'todo-app-88565-firebase-adminsdk-z4fsl-e2a8f69d03.json'
    cred = credentials.Certificate(JSON_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    users = db.collection('tasks')
    docs =users.stream()
    for doc in docs:
        print(users) 

if __name__ == '__main__':
    main2()