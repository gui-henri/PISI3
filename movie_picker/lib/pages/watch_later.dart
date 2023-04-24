import 'package:flutter/material.dart';

class WatchLaterTab extends StatefulWidget {
  static const routeName = '/watch_later';
  const WatchLaterTab({super.key});

  @override
  State<WatchLaterTab> createState() => _WatchLaterTabState();
}

class _WatchLaterTabState extends State<WatchLaterTab> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: const Padding(
              padding: EdgeInsets.fromLTRB(15, 0, 0, 0),
              child: Icon(Icons.movie, size: 40),
            ),
            leadingWidth: 52,
            backgroundColor: Colors.transparent,
            shadowColor: Colors.transparent,
            actions: [
              Padding(
                padding: const EdgeInsets.fromLTRB(15, 0, 10, 0),
                child: IconButton(
                  icon: const Icon(Icons.cancel, size: 40),
                  onPressed: () {
                    Navigator.pop(context);
                  },
                ),
              ),
            ],
        title: const Text('Assistir mais tarde'),
      ),
      body: const Center(
      ),
    );;
  }
}