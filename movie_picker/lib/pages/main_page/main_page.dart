import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:movie_picker/components/movie_search.dart';
import 'package:movie_picker/pages/main_page/explore_tab.dart';
import 'package:movie_picker/pages/main_page/favorites_tab.dart';
import 'package:movie_picker/pages/main_page/settings_tab.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'home_tab.dart';

class MainPage extends StatefulWidget {
  static const routeName = '/main';

  const MainPage({super.key});

  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  int _selectedIndex = 0;

  final _pages = <Widget>[
    const HomeTab(),
    const ExploreTab(),
    const FavoritesTab(),
    const SettingsTab()
  ];

  void refreshFavoritesPage(int value) {
    setState(() {
      if (_selectedIndex == 2){
        _pages.removeAt(2);
        _pages.insert(2, FavoritesTab(key: ObjectKey(_pages[2].hashCode)));
      }
      _selectedIndex = value;
    });
  }

  @override
  Widget build(BuildContext context) {
    final user = ModalRoute.of(context)!.settings.arguments as User;
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
      child: Center(
          child: Column(
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
                    // showSearch() retorna um Future<dynamic>, sendo assim, não podemos ter
                    // certeza do tipo, mas ele deve retornar ou um Movie ou null.
                    // se o usuário entrar na aba de busca, ele deve atualizar os favoritos
                    showSearch(context: context, delegate: MovieSearch())
                        .then((value) => (value != null)
                            ? refreshFavoritesPage(2)
                            : null);
                  },
                ),
              ),
            ],
          ),
          Flexible(
            child: IndexedStack(
              index: _selectedIndex,
              children: _pages,
            ),
          ),
          BottomNavigationBar(
            currentIndex: _selectedIndex,
            onTap: (value) {
              refreshFavoritesPage(value);
            },
            type: BottomNavigationBarType.fixed,
            backgroundColor: const Color.fromARGB(0, 1, 1, 1),
            showSelectedLabels: false,
            showUnselectedLabels: false,
            selectedItemColor: Colors.deepPurpleAccent,
            unselectedItemColor: Colors.white,
            items: const <BottomNavigationBarItem>[
              BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
              BottomNavigationBarItem(
                  icon: Icon(Icons.explore), label: "Explore"),
              BottomNavigationBarItem(
                  icon: Icon(Icons.favorite), label: "Favorite"),
              BottomNavigationBarItem(
                  icon: Icon(Icons.settings), label: "Settings")
            ],
          )
        ],
      )),
    );
  }
}
