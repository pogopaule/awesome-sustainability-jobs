{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        customPython = pkgs.python310.buildEnv.override {
          extraLibs = with pkgs.python310Packages; [
            pytest
            pyyaml
            jinja2
            requests
            oyaml
            selenium
          ];
        };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            customPython
            pkgs.chromedriver
            pkgs.chromium
          ];
        };
      });
}
