{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      pythonReadmeAndMap = pkgs.python3.withPackages (ps: with ps;
        [
          pyyaml
          jinja2
        ]);
      pythonReviews = pkgs.python3.withPackages (ps: with ps;
        [
          requests
          oyaml
          selenium
        ]);
    in
    {
      devShells.${system} = {
        readmeAndMap = pkgs.mkShell {
          buildInputs = [
            pythonReadmeAndMap
          ];
        };
        reviews = pkgs.mkShell {
          buildInputs = [
            pythonReviews
            pkgs.chromedriver
            pkgs.chromium
          ];
        };

      };
    };
}
