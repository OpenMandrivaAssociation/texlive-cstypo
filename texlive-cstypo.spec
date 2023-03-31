Name:		texlive-cstypo
Version:	41986
Release:	2
Summary:	Czech typography rules enforced through LuaTeX hooks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cstypo
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cstypo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cstypo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros that enforce basic Czech
typography rules through Lua hooks available in LuaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/cstypo
%{_texmfdistdir}/tex/lualatex/cstypo
%doc %{_texmfdistdir}/doc/lualatex/cstypo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
