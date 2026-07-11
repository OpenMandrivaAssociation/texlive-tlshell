%global tl_name tlshell
%global tl_revision 78053

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	GUI frontend (tcl/tk-based) for tlmgr
Group:		Publishing
URL:		https://www.ctan.org/pkg/tlshell
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tlshell.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tlshell.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(tlshell.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
GUI frontend (tcl/tk-based) for tlmgr

