import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

enum CardStatus { favorite, description, watchLater, nope }

class CardProvider extends ChangeNotifier {

  List<String> _urlImages = [];
  bool _isDragging = false;
  double _angle = 0;
  Offset _position = Offset.zero;
  Size _screenSize = Size.zero;

  List<String> get urlImages => _urlImages;
  Offset get position => _position;
  bool get isDragging => _isDragging;
  double get angle => _angle;

  CardProvider() {
    resetUsers(); //???
  }

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

    final status = getStatus();

    if (status != null) {
      Fluttertoast.cancel();
      Fluttertoast.showToast(
        msg: status.toString().split('.').last.toUpperCase(),
        fontSize: 36,
      );
    }

    switch (status){
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

  CardStatus? getStatus() {
    final x = _position.dx;
    final y = _position.dy;
    final forceDetails = x.abs() < 20;
    const delta = 100;

    if(x >= delta) {
      return CardStatus.favorite;
    } else if (x <= -delta) {
      return CardStatus.nope;
    } else if (y <= -delta/2 && forceDetails) {
      return CardStatus.description;
    }
  }

  void favorite() {
    _angle = 20;
    _position += Offset(2 * _screenSize.width, 0);
    _nextCard();

    notifyListeners();
  }

  void nope(){
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
    if (_urlImages.isEmpty) return;
    
    // ignore: todo
    // TODO: Adicionar filme no banco de dados
    await Future.delayed(const Duration(milliseconds: 200));
    _urlImages.removeLast();
    resetPosition();
  }

  void resetUsers() {
    _urlImages = <String>[
      'https://i.pinimg.com/236x/e9/11/6c/e9116ce13f29f747d8cc5b2c94a6d556.jpg',
      'https://i.pinimg.com/236x/c9/fc/9d/c9fc9dc8306e8ed2ad87ddf0634a2c08.jpg',
      'https://i.pinimg.com/236x/75/ed/7b/75ed7ba2028bb8cf777235a52f2ecb9e.jpg',
      'https://assets.reedpopcdn.com/glados1.jpg/BROK/resize/1200x1200%3E/format/jpg/quality/70/glados1.jpg',
      'https://i.pinimg.com/564x/03/59/69/0359694907a32c63610b8e7d72b3ed05.jpg'
    ].reversed.toList();

  }

}