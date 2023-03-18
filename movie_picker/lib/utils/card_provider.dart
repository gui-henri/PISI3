import 'package:flutter/material.dart';

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
    resetPosition();
  }

  void resetPosition() {
    _isDragging = false;
    _position = Offset.zero;
    _angle = 0;

    notifyListeners();
  }

  void resetUsers() {
    _urlImages = <String>[
      'https://i.pinimg.com/236x/e9/11/6c/e9116ce13f29f747d8cc5b2c94a6d556.jpg',
      'https://i.pinimg.com/236x/c9/fc/9d/c9fc9dc8306e8ed2ad87ddf0634a2c08.jpg',
      'https://i.pinimg.com/236x/75/ed/7b/75ed7ba2028bb8cf777235a52f2ecb9e.jpg',
    ].reversed.toList();

  }

}