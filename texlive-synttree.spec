%global tl_name synttree
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.2
Release:	%{tl_revision}.1
Summary:	Typeset syntactic trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/synttree
License:	lppl1.3a
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/synttree.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/synttree.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/synttree.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package to typeset syntactic trees such as those used in Chomsky's
Generative grammar, based on a description of the structure of the tree.

