class Portshield < Formula
  desc "Close opened ports (running processes) easily from CLI"
  homepage "https://github.com/ikotun-dev/port.shield"
  url "https://github.com/ikotun-dev/homebrew-portshield/archive/refs/tags/v1.1.2.tar.gz"
  sha256 "ae3c901a8ac2c5f86e06715e0275843d93a85f93c7bd0f237a80d8c4cb2abdcb"
  license "MIT"

  depends_on "python@3.11"

  def install
    python_exec = Formula["python@3.11"].opt_bin/"python3"
    system "#{python_exec}", "-m", "pip", "install", "-r", "requirements.txt"
    bin.install "main.py" => "portshield"
  end
  test do
    assert_match "Usage:", shell_output("#{bin}/portshield --help")
  end
end
