class Myapp < Formula
  desc "CLI app to view and close processes by port number"
  homepage "https://github.com/ikotun-dev/port.shield"
  url "https://github.com/ikotun-dev/port.shield/releases/tag/v1.0.0"
  sha256 "8a1e6c9e444ef0e4b42da267af4ba70102f720957efa3e86f7a67eb85302e745"
  depends_on "python@3.9"

  def install
    bin.install "main"
  end

  test do
    system "#{bin}/main", "--version"
  end
end
