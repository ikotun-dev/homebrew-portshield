class Portshield < Formula
  desc "Close opened ports (running processes) easily from CLI"
  homepage "https://github.com/ikotun-dev/port.shield"
  url "https://github.com/ikotun-dev/homebrew-portshield/archive/refs/tags/v1.1.1.tar.gz"
  sha256 "46926ef81039c26f671a1d98878f8582588b63dcb5e814d96511bdcbe7fcb0cf"
  license "MIT"

  depends_on "python"

  def install
    virtualenv_install_with_resources
    bin.install "main.py" => "portshield"
  
  end

  test do
    assert_match "Usage:", shell_output("#{bin}/portshield --help")
  end
end
