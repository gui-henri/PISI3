import 'package:movie_picker/models/movie.dart';

// Esta classe foi feita com o intuíto de servir como uma interface.  

class MovieDataProvider {
  Future<List<Movie>> fetchMovieListByQuery(String query) {
    return Future.value(<Movie>[]);
  }
}