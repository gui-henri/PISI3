class Providers {
  List<String> streams;

  Providers(this.streams);

  factory Providers.createFromJson(Map<String, dynamic> json, String country) {
    if (json.containsKey(country)) {
      json = json[country];
      if(json.containsKey('flatrate')){
      List<String> streams = [];
      List<dynamic> flatrate = json['flatrate'];
      for (int i = 0; i < flatrate.length; i++) {
        streams.add(flatrate[i]['provider_name']);
      }
      return Providers(streams);
    }
    }
    return Providers(['Indisponivel']);
    }
}