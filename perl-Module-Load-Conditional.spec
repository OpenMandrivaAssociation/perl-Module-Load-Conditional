%define	module	Module-Load-Conditional
%define	name	perl-%{module}
%define	version	0.22
%define	release	%mkrel 1

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Looking up module information / loading at runtime
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl(Module::Load)
Buildrequires:	perl(Params::Check)
Buildrequires:	perl-version
Buildarch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Module::Load::Conditional provides simple ways to query and possibly load any
of the modules you have installed on your system during runtime.

It is able to load multiple modules at once or none at all if one of them was
not able to load. It also takes care of any error checking and so forth.

It allows you to fetch any file pointed to by a ftp, http, file, or rsync uri
by a number of different means.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Module
%{_mandir}/*/*


