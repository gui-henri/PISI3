import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/tmdb_service_provider.dart';
import '../services/firestore_services_provider.dart';
import 'dart:math';

enum CardStatus { favorite, description, watchLater, nope }

class CardProvider extends ChangeNotifier {
  List<Movie> _movies = [];
  bool _isDragging = false;
  double _angle = 0;
  Offset _position = Offset.zero;
  Size _screenSize = Size.zero;

  final yuri = TmdbServiceProvider();
  final db = FiresStoreServiceProvider();

  List<Movie> get movies => _movies;
  Offset get position => _position;
  bool get isDragging => _isDragging;
  double get angle => _angle;

  CardProvider() {
   fetchRecomendations(); //???
  }

  get status => null;

  void setScreenSize(Size screenSize) => _screenSize = screenSize;

  void startPosition(DragStartDetails details) {
    _isDragging = true;
    notifyListeners();
  }

  void updatePosition(DragUpdateDetails details) {
    _position += details.delta;

    final x = _position.dx;
    _angle = 45 * x / _screenSize.width;
    notifyListeners();
  }

  void endPosition() {
    _isDragging = false;
    notifyListeners();

    final status = getStatus(force: true);

    if (status != null) {
      Fluttertoast.cancel();
      Fluttertoast.showToast(
        msg: status.toString().split('.').last.toUpperCase(),
        fontSize: 36,
      );
    }

    switch (status) {
      case CardStatus.favorite:
        favorite();
        break;
      case CardStatus.nope:
        nope();
        break;
      case CardStatus.description:
        description();
        break;
      default:
        resetPosition();
    }
  }

  void resetPosition() {
    _isDragging = false;
    _position = Offset.zero;
    _angle = 0;

    notifyListeners();
  }

  CardStatus? getStatus({bool force = false}) {
    final x = _position.dx;
    final y = _position.dy;
    final forceDetails = x.abs() < 20;

    if (force) {
      final delta = 100;

      if (x >= delta) {
        return CardStatus.favorite;
      } else if (x <= -delta) {
        return CardStatus.nope;
      } else if (y <= -delta / 2 && forceDetails) {
        return CardStatus.description;
      }
    } else {
      final delta = 20;

      if (y <= -delta * 2 && forceDetails) {
        return CardStatus.description;
      } else if (x >= delta) {
        return CardStatus.favorite;
      } else if (x <= -delta) {
        return CardStatus.nope;
      }
    }
  }

  void favorite() {
    _angle = 20;
    _position += Offset(2 * _screenSize.width, 0);
    _nextCard();

    notifyListeners();
  }

  void nope() {
    _angle = -20;
    _position -= Offset(2 * _screenSize.width, 0);
    _nextCard();

    notifyListeners();
  }

  void description() {
    _angle = 0;
    _position -= Offset(0, _screenSize.height);
    _nextCard();

    notifyListeners();
  }

  Future _nextCard() async {
    if (_movies.isEmpty) return;

    // ignore: todo
    // TODO: Adicionar filme no banco de dados
    await Future.delayed(const Duration(milliseconds: 200));
    _movies.removeLast();
    resetPosition();
  }

  Future<void> fetchRecomendations() async {

    // pega os favoritos do usuário
      // se o usuário não tem favoritos, pega os mais populares
    // pega um id aleatório entre os favoritos do usuáiro
    // recomenda 15 filmes com base nesse filme
    // quando estiver nos últimos 5 filmes, pega mais 15 de outro filme

    final favorites = await db.obterFilmes();

    if (favorites.isNotEmpty) {
      final randIndex = Random().nextInt(favorites.length);
      _movies = await yuri.fetchMovieRecommendationsById(favorites[randIndex].id.toString());
    } else {
      final ciel = TmdbServiceProvider();
      final lulaFazueli = await ciel.fetchMostPopular();
      final randi = Random().nextInt(lulaFazueli.length);
      _movies = await yuri.fetchMovieRecommendationsById(favorites[randi].id.toString());
    }

    notifyListeners();
  }
}
