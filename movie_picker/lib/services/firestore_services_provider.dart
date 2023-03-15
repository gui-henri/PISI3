import 'package:firebase_auth/firebase_auth.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/interfaces/db_provider.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class FiresStoreServiceProvider implements DbProvider {
  final db = FirebaseFirestore.instance;

  @override
  Future<void> adicionarFilme(Movie movie) async {
    final daoMovie = <String, String>{
      "img_url": movie.posterPath,
      "name": movie.title
    };

    final user = FirebaseAuth.instance.currentUser;

    if (user != null) {
      db
          .collection("users")
          .doc(user.uid)
          .collection("movies")
          .doc(movie.id.toString())
          .set(daoMovie);
    }
  }

  @override
  Future<List<Movie>> obterFilmes() async {
    return Future.value(<Movie>[]);
  }

  @override
  Future<void> removerFilme(Movie movie) async {
    final user = FirebaseAuth.instance.currentUser;

    if (user != null) {
      db
          .collection("users")
          .doc(user.uid)
          .collection("movies")
          .doc(movie.id.toString())
          .delete();
    }
  }
}
