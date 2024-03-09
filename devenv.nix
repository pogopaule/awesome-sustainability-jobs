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

  scripts = {
    create_readme.exec = ''
      pushd src > /dev/null &&
      python create_readme.py &&
      popd > /dev/null
    '';
    create_map_data.exec = ''
      pushd src > /dev/null &&
      python create_map_data.py &&
      popd > /dev/null
    '';
    update_reviews.exec = ''
      pushd src > /dev/null &&
      python update_reviews.py &&
      popd > /dev/null
    '';
    run_tests.exec = "pytest src/test_all.py";
  };
}
