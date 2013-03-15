%define		_class		DB
%define		_subclass	QueryTool
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.2
Release:	9
Summary:	An OO-interface for easily retrieving and modifying data in a DB
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_QueryTool/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package is an OO-abstraction to the SQL-Query language, it
provides methods such as setWhere, setOrder, setGroup, setJoin, etc.
to easily build queries. It also provides an easy to learn interface
that interacts nicely with HTML-forms using arrays that contain the
column data, that shall be updated/added in a DB. This package bases
on an SQL-Builder which lets you easily build SQL-Statements and
execute them.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-7mdv2012.0
+ Revision: 741843
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-6
+ Revision: 679287
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-5mdv2011.0
+ Revision: 613628
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-4mdv2010.1
+ Revision: 479295
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.1.2-3mdv2010.0
+ Revision: 441000
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-2mdv2009.1
+ Revision: 321955
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-1mdv2009.0
+ Revision: 278913
- update to new version 1.1.2

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-9mdv2009.0
+ Revision: 236824
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.11.1-8mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-8mdv2007.0
+ Revision: 81489
- Import php-pear-DB_QueryTool

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-1mdk
- initial Mandriva package (PLD import)

