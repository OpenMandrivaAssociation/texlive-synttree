Name:		texlive-synttree
Version:	16252
Release:	2
Summary:	Typeset syntactic trees
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/synttree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synttree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synttree.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synttree.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to typeset syntactic trees such as those used in
Chomsky's Generative grammar, based on a description of the
structure of the tree.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/synttree/synttree.sty
%doc %{_texmfdistdir}/doc/latex/synttree/README
%doc %{_texmfdistdir}/doc/latex/synttree/synttree.pdf
#- source
%doc %{_texmfdistdir}/source/latex/synttree/synttree.dtx
%doc %{_texmfdistdir}/source/latex/synttree/synttree.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
