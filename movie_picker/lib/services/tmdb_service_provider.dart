import 'dart:convert';

import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/interfaces/movie_data_provider.dart';
import 'package:http/http.dart' as http;

class TmdbServiceProvider implements MovieDataProvider{

  final tmdbKey = dotenv.env['TMDB_API_KEY'];

  @override
  Future<List<Movie>> fetchMovies(String query) async {
    final ulr = 'https://api.themoviedb.org/3/search/movie?api_key=$tmdbKey&query=$query';
    final response = await http.get(Uri.parse(ulr));
    if(response.statusCode == 200) {
      final json = jsonDecode(response.body);
      return Movie.fromJsonToObjectList(json['results']); 
    } else {
      return Future.error(
        Exception(
          'Error fetching movies. Movie data could not be fetched because server did not respond with code 200.'
        )
      );
    }
  }
}