import 'package:flutter/material.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/interfaces/movie_data_provider.dart';
import 'package:movie_picker/services/tmdb_service_provider.dart';
import 'package:movie_picker/utils/search_result.dart';


class MovieSearchController {

  Set<SearchResult<List<Movie>>> searchHistory = Set.identity();
  MovieDataProvider provider = TmdbServiceProvider();

  Future<SearchResult<List<Movie>>> searchMovieByQuery(String query, BuildContext context) async {
    try {
      if (query.isNotEmpty) {
        bool didFetched = false;
        List<Movie> movieList = [];
        final queryExistsOnHistory = searchHistory.where((searchResult) => searchResult.query == query);

        if (queryExistsOnHistory.isEmpty) {
          // caso não haja nenhuma pesquisa com a mesma query
          movieList = await provider.fetchMovies(query);
          didFetched = true;
          searchHistory.add(SearchResult(query, didFetched, movieList));
        } else {
          movieList = queryExistsOnHistory.first.data;
        }

        return SearchResult(query, didFetched, movieList);

      } 
    } catch (e) {
      final errorMessage = e.toString();
      showDialog(
        context: context, 
        builder: ((context) {
          return AlertDialog(
            title: const Text("Error"),
            content: SingleChildScrollView(
              child: ListBody(
                children: <Widget>[
                  Text("An error ocourred during the search. This is the error message: $errorMessage")
                ],
              ),
            ),
          );
        })
      );
    }
    return SearchResult(query, false, <Movie>[]);
  }
}