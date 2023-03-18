import 'package:flutter/material.dart';

class CardProvider extends ChangeNotifier {

  bool _isDragging = false;
  Offset _position = Offset.zero;
  Offset get position => _position;
  bool get isDragging => _isDragging;

  void startPosition(DragStartDetails details) {
    _isDragging = true;
    notifyListeners();
  }
  void updatePosition(DragUpdateDetails details) {
    _position += details.delta;
    notifyListeners();
  }
  void endPosition() {
    resetPosition();
  }

  void resetPosition() {
    _isDragging = false;
    _position = Offset.zero;
    notifyListeners();
  }

}