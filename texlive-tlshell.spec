Name:		texlive-tlshell
Version:	62795
Release:	2
Summary:	GUI frontend (tcl/tk-based) for tlmgr
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tlshell
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlshell.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlshell.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/tlshell
%doc %{_texmfdistdir}/texmf-dist/doc/support/tlshell

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
