class SearchResult<T> {
  String query;
  bool didFetched;
  T data;

  SearchResult(this.query, this.didFetched, this.data);
}