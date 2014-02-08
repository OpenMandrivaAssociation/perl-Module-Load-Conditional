%define	upstream_name	 Module-Load-Conditional
%define upstream_version 0.46

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.460.0-4
+ Revision: 765489
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.460.0-3
+ Revision: 764840
- rebuild

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.460.0-2
+ Revision: 763984
- rebuilt for perl-5.14.x

* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.460.0-1
+ Revision: 759450
- version update 0.46

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.440.0-2
+ Revision: 667261
- mass rebuild

* Sat Feb 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.440.0-1
+ Revision: 637375
- update to new version 0.44

* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.400.0-1mdv2011.0
+ Revision: 630632
- update to new version 0.40

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-3mdv2011.0
+ Revision: 562432
- rebuild

* Sat Jul 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-2mdv2011.0
+ Revision: 558167
- rebuild

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.1
+ Revision: 539059
- update to 0.38

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-2mdv2010.1
+ Revision: 519946
- rebuild with new rpm-setup

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.1
+ Revision: 503733
- update to 0.36

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2010.1
+ Revision: 461329
- update to 0.34

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 405943
- rebuild using %%perl_convert_version

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2009.1
+ Revision: 331587
- update to new version 0.30

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2009.1
+ Revision: 320437
- update to new version 0.28

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.26-4mdv2009.0
+ Revision: 257898
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.26-3mdv2009.0
+ Revision: 245944
- rebuild

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 0.26-1mdv2008.1
+ Revision: 177286
- update to new version 0.26

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2008.1
+ Revision: 152838
- update to new version 0.24

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2008.1
+ Revision: 104493
- update to new version 0.22

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2008.1
+ Revision: 97516
- update to new version 0.20


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2007.0
+ Revision: 133743
- fix build dependencies
- new version
- Import perl-Module-Load-Conditional

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2007.0
- New version 0.12

* Sat Aug 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2007.0
- New version 0.10

* Fri May 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-2mdk
- buildrequires fix

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdk
- first mdk release

