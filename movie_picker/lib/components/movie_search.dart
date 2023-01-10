import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:http/http.dart' as http;
import 'package:movie_picker/utils/movie.dart';

class MovieSearch extends SearchDelegate {

  Future<List<Movie>> fetchMovies(String query) async {
    if (query.isNotEmpty) {
      String ulr = 'https://api.themoviedb.org/3/search/movie?api_key=TMDB_API_KEY&query=$query';
      final response = await http.get(Uri.parse(ulr));
      if(response.statusCode == 200) {
        final json = jsonDecode(response.body);
        return Movie.fromJsonToObjectList(json['results']);
      } else {
        throw Exception('Failed to load movie search');
      }
    }
    return <Movie>[];
  }

  @override
  ThemeData appBarTheme(BuildContext context) {
    return ThemeData(
      appBarTheme: const AppBarTheme(
        backgroundColor: Color.fromARGB(255, 31, 3, 88),
      ),
      textTheme: const TextTheme(
        headline6: TextStyle(
          fontSize: 18,
          color: Colors.white
        )
      ),
      inputDecorationTheme: const InputDecorationTheme(
        border: InputBorder.none,
        hintStyle: TextStyle(
          color: Colors.white60
        )
      )
    );
  }

  @override
  List<Widget>? buildActions(BuildContext context) {
    return [
      IconButton(
        icon: const Icon(Icons.clear),
        onPressed: () { 
          if (query.isEmpty) {
            close(context, null);
          } else {
            query = '';
          }
        }
      )
    ];
  }

  @override
  Widget? buildLeading(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.arrow_back),
      onPressed: () => close(context, null)
    );
  }

  @override
  Widget buildResults(BuildContext context) {
    if (query.isEmpty) {
      return Container(
        decoration: mpDefaultBackgroundDecoration(),
      );
    }
    return FutureBuilder(
      future: fetchMovies(query),
      builder: ((context, snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          return ListView.builder(
            itemCount: snapshot.data!.length,
            itemBuilder: (context, index) {
              return _filmResult(snapshot.data![index]);
            },
          );
        } else {
          return const Center(child: CircularProgressIndicator());
        }
      }),
    );
  }

  @override
  Widget buildSuggestions(BuildContext context) {
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
    );
  }

  ListTile _filmResult(Movie movie) {
    return ListTile(
      title: Text(movie.title),
    );
  }

}