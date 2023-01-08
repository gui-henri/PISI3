import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';

class MovieSearch extends SearchDelegate {

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
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
    );
  }

  @override
  Widget buildSuggestions(BuildContext context) {
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
    );
  }

}