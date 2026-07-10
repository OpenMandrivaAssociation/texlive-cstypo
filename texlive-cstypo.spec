%global tl_name cstypo
%global tl_revision 41986

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.03
Release:	%{tl_revision}.1
Summary:	Czech typography rules enforced through LuaTeX hooks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/cstypo
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cstypo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cstypo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros that enforce basic Czech typography rules
through Lua hooks available in LuaTeX.

