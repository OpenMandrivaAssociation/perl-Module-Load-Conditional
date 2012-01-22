%define	upstream_name	 Module-Load-Conditional
%define upstream_version 0.46

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:	Looking up module information / loading at runtime
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl-devel
Buildrequires:	perl(Module::Load)
Buildrequires:	perl(Params::Check)
Buildrequires:	perl(version)

Buildarch:	    noarch

%description
Module::Load::Conditional provides simple ways to query and possibly load any
of the modules you have installed on your system during runtime.

It is able to load multiple modules at once or none at all if one of them was
not able to load. It also takes care of any error checking and so forth.

It allows you to fetch any file pointed to by a ftp, http, file, or rsync uri
by a number of different means.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Module
%{_mandir}/*/*
