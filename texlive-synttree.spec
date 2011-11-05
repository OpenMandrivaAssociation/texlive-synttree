# revision 16252
# category Package
# catalog-ctan /macros/latex/contrib/synttree
# catalog-date 2009-11-30 09:23:31 +0100
# catalog-license lppl
# catalog-version 1.4.2
Name:		texlive-synttree
Version:	1.4.2
Release:	1
Summary:	Typeset syntactic trees
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/synttree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synttree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synttree.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synttree.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package to typeset syntactic trees such as those used in
Chomsky's Generative grammar, based on a description of the
structure of the tree.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/synttree/synttree.sty
%doc %{_texmfdistdir}/doc/latex/synttree/README
%doc %{_texmfdistdir}/doc/latex/synttree/synttree.pdf
#- source
%doc %{_texmfdistdir}/source/latex/synttree/synttree.dtx
%doc %{_texmfdistdir}/source/latex/synttree/synttree.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}