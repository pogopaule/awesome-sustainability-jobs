{ pkgs, ... }:

{
  packages = [
    pkgs.chromedriver
    # pkgs.chromium
  ];

  languages.python = {
    enable = true;
    venv = {
      enable = true;
      requirements = ''
        requests
        oyaml
        selenium
        pytest
        pyyaml
        jinja2
      '';
    };
  };
}
