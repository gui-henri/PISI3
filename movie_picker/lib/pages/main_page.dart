import 'package:flutter/material.dart';
import 'package:movie_picker/pages/explore_page.dart';
import 'package:movie_picker/pages/favorites_page.dart';
import 'package:movie_picker/pages/settings_page.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'home_page.dart';

class MainPage extends StatefulWidget {
  const MainPage({super.key});

  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {

  int _selectedIndex = 0;

  final _pages = const <Widget>[
    HomePage(),
    ExplorePage(),
    FavoritesPage(),
    SettingsPage()
  ];

  @override
  Widget build(BuildContext context) {

    return Container(
      decoration: mpDefaultBackgroundDecoration(),
      child: Center(
        child: 
          Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              AppBar(
                title: const Text("MoviePicker"),
              ),
              IndexedStack(
                index: _selectedIndex,
                children: _pages,
              ),
              BottomNavigationBar(
                currentIndex: _selectedIndex,
                onTap: (value) {
                  setState(() {
                    _selectedIndex = value;
                  });
                },
                type: BottomNavigationBarType.fixed,
                
                backgroundColor: const Color.fromARGB(0, 1, 1, 1),
                showSelectedLabels: false,
                showUnselectedLabels: false,
                selectedItemColor: Colors.deepPurpleAccent,
                unselectedItemColor: Colors.white,
                items: const <BottomNavigationBarItem>[
                  BottomNavigationBarItem(
                    icon: Icon(Icons.home),
                    label: "Home"
                  ),
                  BottomNavigationBarItem(
                    icon: Icon(Icons.compass_calibration),
                    label: "Explore"
                  ),
                  BottomNavigationBarItem(
                    icon: Icon(Icons.favorite),
                    label: "Favorite"
                  ),
                  BottomNavigationBarItem(
                    icon: Icon(Icons.settings),
                    label: "Settings"
                  )
                ],
              )
            ],
          )
        ),
    );
  }
}