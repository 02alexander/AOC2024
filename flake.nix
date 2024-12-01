{
  description = "Development shell for AOC";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: 
      let 
        pkgs = nixpkgs.legacyPackages.${system};
        python-packages = ps: with ps; [
          numpy
          z3
          matplotlib
        ];
      in {
        devShell = pkgs.mkShell {
          buildInputs = [
            (pkgs.python311.withPackages python-packages)
            pkgs.cargo-watch
            pkgs.entr
          ];
        };
      } 
    );
}
