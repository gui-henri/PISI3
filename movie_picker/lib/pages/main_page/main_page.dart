import 'package:flutter/material.dart';
import 'package:movie_picker/components/movie_search.dart';
import 'package:movie_picker/pages/main_page/explore_tab.dart';
import 'package:movie_picker/pages/main_page/favorites_tab.dart';
import 'package:movie_picker/pages/main_page/settings_tab.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'home_tab.dart';

class MainPage extends StatefulWidget {
  const MainPage({super.key});

  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {

  int _selectedIndex = 0;

  final _pages = const <Widget>[
    HomeTab(),
    ExploreTab(),
    FavoritesTab(),
    SettingsTab()
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
                      icon: const Icon(Icons.search, size: 40),
                      onPressed: () {
                         final movieToShow = showSearch(
                          context: context, 
                          delegate: MovieSearch()
                        );
                        movieToShow.then((movie) => debugPrint(movie.title));
                      },
                    ),
                  ),
                ],
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