import 'package:flutter/material.dart';
import '../models/movie.dart';
import '../services/firestore_services_provider.dart';
import '../services/tmdb_service_provider.dart';
import 'movie_page.dart';

class WatchLaterTab extends StatefulWidget {
  static const routeName = '/watch_later';
  const WatchLaterTab({super.key});

  @override
  State<WatchLaterTab> createState() => _WatchLaterTabState();
}

class _WatchLaterTabState extends State<WatchLaterTab> {
  @override
  Widget build(BuildContext context) {
    final db = FiresStoreServiceProvider();

    final Future<List<Movie>> toWatchLater = db.obterFilmesWatchLater();
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
      body: FutureBuilder(
        future: toWatchLater,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            if (snapshot.data!.isEmpty) {
              return const Center(
                child: Padding(
                  padding: EdgeInsets.all(28),
                  child: Text(
                    "Você não tem filmes para assistir mais tarde ainda!",
                    style: TextStyle(
                        fontSize: 16,
                        decoration: TextDecoration.none,
                        color: Colors.white),
                  ),
                ),
              );
            }else {
              return GridView.builder(
                gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
                  maxCrossAxisExtent: 140,
                  childAspectRatio: 0.65,
                  crossAxisSpacing: 4,
                  mainAxisSpacing: 2
                  ),
                itemCount: snapshot.data!.length,
                itemBuilder: (BuildContext ctx, index) {
                return Container(
                  margin: const EdgeInsets.all(7.5),
                  alignment: Alignment.bottomRight,
                  decoration: BoxDecoration(
                   color: Colors.transparent,
                   borderRadius: BorderRadius.circular(10)),
                   child: Column(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                     children: [Stack(
                      children: [GestureDetector(
                        onTap: () async {
                          final provider = TmdbServiceProvider();
                          provider
                          .fetchMovieById(snapshot.data![index].id
                          .toString())
                          .then((value) {
                            Navigator.pushNamed(
                              context, MoviePage.routeName,arguments: value);
                                            }
                                            );
                                          },
                                          child: ClipRRect(
                                            borderRadius:
                                                BorderRadius.circular(10),
                                            child: AspectRatio(
                                              aspectRatio:
                                                  0.7, // Defina a proporção que você deseja manter
                                              child: snapshot.data != null
                                                  ? Image.network(
                                                      "https://image.tmdb.org/t/p/w500${snapshot.data![index].posterPath}",
                                                      fit: BoxFit.cover,
                                                      errorBuilder:
                                                          (BuildContext context,
                                                              Object exception,
                                                              StackTrace?
                                                                  stackTrace) {
                                                        return Image.network(
                                                          "https://ih1.redbubble.net/image.1304795334.8057/fposter,small,wall_texture,product,750x1000.jpg", // caminho para a imagem padrão
                                                          fit: BoxFit.cover,
                                                        );
                                                      },
                                                    )
                                                  : Image.network(
                                                      "https://ih1.redbubble.net/image.1304795334.8057/fposter,small,wall_texture,product,750x1000.jpg", // caminho para a imagem padrão
                                                      fit: BoxFit.cover,
                                                    ),
                                            ),
                                          ),
                                        ),
                                        Positioned(
                                          bottom: 5,
                                          right: 5,
                                          child: IconButton(
                                            onPressed: () async {
                                              await db.removerFilmeWatchLater(
                                                  snapshot.data![index]);
                                              setState(() {});
                                            },
                                            icon: const Icon(Icons.watch_later,
                                                color: Color.fromARGB(255, 216, 165, 26)),
                                            padding: EdgeInsets.zero,
                                            constraints: const BoxConstraints(),
                                            splashRadius: 15,
                                            iconSize: 22,
                                          ),
                                        ),
                                      ],
                                    )
                                  ],
                                )
                                );
                          }
                );
            }
          }
          else {
            return const CircularProgressIndicator();
          }
        },
        
      ),
    );;
  }
}