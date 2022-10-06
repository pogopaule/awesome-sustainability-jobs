{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      python = pkgs.python3.withPackages (ps: with ps;
        [
          pytest
          pyyaml
          jinja2
          requests
          oyaml
          selenium
        ]);
    in
    {
      devShell.${system} = pkgs.mkShell {
        buildInputs = [
          python
          pkgs.chromedriver
          pkgs.chromium
        ];
      };
    };
}
