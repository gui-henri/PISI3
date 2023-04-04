import 'package:movie_picker/models/movie.dart';

// Esta classe foi feita com o intuíto de servir como uma interface.  

class MovieDataProvider {

  Future<Movie> fetchMovieById(String id){
    return Future.value(Movie(id: 0, title: 'untitled'));
  }

  Future<List<Movie>> fetchMovieListByQuery(String query) {
    return Future.value(<Movie>[]);
  }

  Future<String> fetchMovieProviders(int id, {String country = 'BR'}) {
    return Future.value('');
  }

  Future<List<Movie>> fetchMostPopular() {
    return Future.value(<Movie>[]);
  }
}