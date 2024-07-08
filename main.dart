import 'package:firebase_dart/firebase_dart.dart';

void main() async {
  FirebaseApp app = await Firebase.initializeApp(
    options: FirebaseOptions(
      apiKey: 'your-api-key',
      authDomain: 'your-project-id.firebaseapp.com',
      projectId: 'your-project-id',
      storageBucket: 'your-project-id.appspot.com',
      messagingSenderId: 'your-messaging-sender-id',
      appId: 'your-app-id',
    ),
  );

  FirebaseFirestore firestore = FirebaseFirestore.instanceFor(app: app);

  // Firestore 에뮬레이터 설정
  firestore.settings = Settings(
    host: 'localhost:8080',
    sslEnabled: false,
  );

  // Firestore에 데이터 추가 예제
  CollectionReference users = firestore.collection('users');
  await users.add({'name': 'John Doe', 'email': 'johndoe@example.com'});
}
