import 'package:movie_picker/models/movie.dart';

// Esta classe foi feita com o intuíto de servir como uma interface.

class DbProvider {
  Future<void> adicionarFilme(Movie movie) async {}
  Future<void> removerFilme(Movie movie) async {}
  Future<List<Movie>> obterFilmes() async {
    return Future.value(<Movie>[]);
  }
  Future<void> adicionarFilmeWatchLater(Movie movie) async {}
  Future<List<Movie>> obterFilmesWatchLater() async {
    return Future.value(<Movie>[]);
  }
  Future<void> removerFilmeWatchLater(Movie movie) async {}


}
