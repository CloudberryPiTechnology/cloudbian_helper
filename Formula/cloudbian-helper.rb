class CloudbianHelper < Formula
  include Language::Python::Virtualenv

  desc "Cloudbian Helper CLI tool"
  homepage "https://github.com/CloudberryPiTechnology/cloudbian_helper"
  url "https://github.com/CloudberryPiTechnology/cloudbian_helper/releases/download/v0.1.2/cloudbian_helper-0.1.2.tar.gz"
  sha256 "30c23c27d33cd780d4c706fd56b0073f9ab49bebf2229395e018c48bd142aa8f"
  license "MIT"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/cloudbian-helper"
  end
end
