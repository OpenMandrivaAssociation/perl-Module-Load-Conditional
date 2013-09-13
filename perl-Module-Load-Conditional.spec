%define	modname	Module-Load-Conditional
%define modver	0.46

Summary:	Looking up module information / loading at runtime
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{modver}.tar.gz
Buildarch:	noarch
Buildrequires:	perl-devel
Buildrequires:	perl(Module::Load)
Buildrequires:	perl(Params::Check)
Buildrequires:	perl(version)

%description
Module::Load::Conditional provides simple ways to query and possibly load any
of the modules you have installed on your system during runtime.

It is able to load multiple modules at once or none at all if one of them was
not able to load. It also takes care of any error checking and so forth.

It allows you to fetch any file pointed to by a ftp, http, file, or rsync uri
by a number of different means.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Module
%{_mandir}/man3/*

