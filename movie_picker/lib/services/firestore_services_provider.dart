import 'package:firebase_auth/firebase_auth.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/interfaces/db_provider.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:movie_picker/services/interfaces/movie_data_provider.dart';
import 'package:movie_picker/services/tmdb_service_provider.dart';

class FiresStoreServiceProvider implements DbProvider {
  final db = FirebaseFirestore.instance;
  final MovieDataProvider tmdb = TmdbServiceProvider();

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

  Future<void> adicionarFilmeWatchLater(Movie movie) async {
    final daoMovie = <String, String>{
      "img_url": movie.posterPath,
      "name": movie.title
    };

    final user = FirebaseAuth.instance.currentUser;

    if (user != null) {
      db
          .collection("users")
          .doc(user.uid)
          .collection("watch_later")
          .doc(movie.id.toString())
          .set(daoMovie);
    }
  }

  @override
  Future<List<Movie>> obterFilmes() async {
    final user = FirebaseAuth.instance.currentUser;

    if (user == null) {
      return Future.error(Exception('Usuário não existe, impossível buscar favoritos'));
    }
    const source = Source.cache;

    final querySnapshot = await db
      .collection("users")
      .doc(user.uid)
      .collection("movies")
      .get(const GetOptions(source: source));

    final data = querySnapshot.docs.map((doc) => {
        ...doc.data(),
        'id': doc.id
       }).toList();
      
    final movies = data.map((document) => 
      Movie.fromJson({
        'id': int.parse(document['id']),
        'title': document['name'],
        'poster_path': document['img_url']
      })).toList();
    return movies;
  }

  Future<List<Movie>> obterFilmesWatchLater() async {
    final user = FirebaseAuth.instance.currentUser;

    if (user == null) {
      return Future.error(Exception('Usuário não existe, impossível buscar favoritos'));
    }
    const source = Source.cache;

    final querySnapshot = await db
      .collection("users")
      .doc(user.uid)
      .collection("watch_later")
      .get(const GetOptions(source: source));

    final data = querySnapshot.docs.map((doc) => {
        ...doc.data(),
        'id': doc.id
       }).toList();
      
    final movies = data.map((document) => 
      Movie.fromJson({
        'id': int.parse(document['id']),
        'title': document['name'],
        'poster_path': document['img_url']
      })).toList();
    return movies;
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

  Future<void> removerFilmeWatchLater(Movie movie) async {
    final user = FirebaseAuth.instance.currentUser;

    if (user != null) {
      db
          .collection("users")
          .doc(user.uid)
          .collection("watch_later")
          .doc(movie.id.toString())
          .delete();
    }
  }
}
