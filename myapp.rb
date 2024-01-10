class Myapp < Formula
  desc "Command line tool to view your running proccess with their PIDS and ports and also kill the process if you want to."
  homepage "https://github.com/ikotun-dev/port.shield"
  url "https://github.com/ikotun-dev/port.shield/archive/refs/tags/v1.1.0.zip"
  sha256 "6716c58c87d7c2ffd93afe2adcd4610c6016fa889d604430f3869d71f52735b5"
  depends_on "python@3.9"

 
 def install
    bin.install "main.py" => "killport"  # Update with your script filename
  end

  test do
    system "#{bin}/main", "--version"
  end
end
