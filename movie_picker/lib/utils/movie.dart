
class Movie {
  final String? posterPath;
  final bool? adult;
  final String? overview;
  final String? releaseDate;
  final List<dynamic> genreIds;
  final int? id;
  final String? originalTitle;
  final String? originalLanguage;
  final String title;
  final String? backdropPath;
  final dynamic popularity;
  final int? voteCount;
  final dynamic voteAverage;

  const Movie({
    required this.id,
    required this.posterPath,
    required this.adult,
    required this.overview,
    required this.releaseDate,
    required this.genreIds,
    required this.originalTitle,
    required this.originalLanguage,
    required this.title,
    required this.backdropPath,
    required this.popularity,
    required this.voteAverage,
    required this.voteCount
  });

  factory Movie.fromJson(Map<String, dynamic> json){
    return Movie(
      id: json['id'], 
      posterPath: json['poster_path'], 
      adult: json['adult'], 
      overview: json['overview'], 
      releaseDate: json['release_date'],
      genreIds: json['genre_ids'], 
      originalTitle: json['original_title'], 
      originalLanguage: json['original_language'], 
      title: json['title'], 
      backdropPath: json['backdrop_path'], 
      popularity: json['popularity'], 
      voteAverage: json['vote_average'] , 
      voteCount: json['vote_count']
    );
    
  }

  static fromJsonToObjectList(List<dynamic> movies){

    List<Movie> movieObjects = [];
    for (var movie in movies) {
        movieObjects.add(Movie.fromJson(movie));
    }
    return movieObjects;
  }
}