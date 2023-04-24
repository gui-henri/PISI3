import 'package:flutter/material.dart';

class WatchLaterTab extends StatefulWidget {
  const WatchLaterTab({super.key});

  @override
  State<WatchLaterTab> createState() => _WatchLaterTabState();
}

class _WatchLaterTabState extends State<WatchLaterTab> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Assistir mais tarde'),
      ),
      body: Center(
      ),
    );;
  }
}