class Movie {
  String posterPath;
  bool adult;
  String overview;
  String releaseDate;
  List<int> genreIds;
  int id;
  String originalTitle;
  String originalLanguage;
  String title;
  String backdropPath;
  double popularity;
  int voteCount;
  double voteAverage;


  /*  
      Caso os dados estejam vindo de uma API, não é recomendado instanciar a classe diretamente,
      pois os valores da API podem ser null e causarem erros na instanciação. Para garantir o funcionamento
      nesses casos, utilize o método estático Movie.create(), que vai realizar as devidas checagens e evitar erros
      de tipagem e null-safety.
  */ 
  Movie({
    required this.id,
    this.posterPath = "",
    this.adult = false,
    this.overview = "Unavailable overview",
    this.releaseDate = "Unavailable release date",
    this.genreIds = const <int>[],
    this.originalTitle = "Original title not available",
    this.originalLanguage = "Original language not available",
    required this.title,
    this.backdropPath = "",
    this.popularity = 0.0,
    this.voteAverage = 0.0,
    this.voteCount = 0
  });

  factory Movie.create(
    int id,
    String title,
    {
      String? posterPath,
      bool? adult,
      String? overview,
      String? releaseDate,
      List<int>? genreIds,
      String? originalTitle,
      String? originalLanguage,
      String? backdropPath,
      dynamic popularity,
      dynamic voteAverage,
      int? voteCount
    }
  ) {
    return Movie(
      id: id, 
      title: title,
      posterPath: (posterPath != null) ? posterPath : "",
      adult: (adult != null) ? adult : false,
      overview: (overview != null) ? overview : "Unavailable overview",
      releaseDate: (releaseDate != null) ? releaseDate : "Unavailable release date",
      genreIds: (genreIds != null) ? genreIds : const <int>[],
      originalTitle: (originalTitle != null) ? originalTitle : "Original title not available",
      backdropPath: (backdropPath != null) ? backdropPath : "Original language not available",
      popularity: (popularity != null) ? popularity.toDouble() : 0.0,
      voteAverage: (voteAverage != null) ? voteAverage.toDouble() : 0.0,
      voteCount: (voteCount != null) ? voteCount.toInt() : 0,
    );
  }

  factory Movie.fromJson(Map<String, dynamic> json){
    return Movie.create(
      json['id'], 
      json['title'], 
      posterPath: json['poster_path'], 
      adult: json['adult'], 
      overview: json['overview'], 
      releaseDate: json['release_date'],
      genreIds: (json['genre_ids'] != null) ? json['genre_ids'].cast<int>() : null, 
      originalTitle: json['original_title'], 
      originalLanguage: json['original_language'], 
      backdropPath: json['backdrop_path'], 
      popularity: json['popularity'], 
      voteAverage: json['vote_average'] , 
      voteCount: json['vote_count']
    );
  }

  static List<Movie> fromJsonToObjectList(List<dynamic> movies){

    List<Movie> movieObjects = [];
    for (var movie in movies) {
        movieObjects.add(Movie.fromJson(movie));
    }
    return movieObjects;
  }
}