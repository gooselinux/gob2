Summary: The GObject Builder
Name: gob2
Version: 2.0.16
Release: 5%{?dist}
License: GPLv2+
Group: Development/Tools
Source: http://ftp.5z.com/pub/gob/gob2-%{version}.tar.gz
Url: http://www.5z.com/jirka/gob.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glib2-devel 
BuildRequires: bison flex
Patch0: gob2-remove_sep.patch

%description
GOB is a simple preprocessor for making GObject objects (glib objects).
It makes objects from a single file which has inline C code so that
you don't have to edit the generated files.  Syntax is somewhat inspired
by java and yacc.  It supports generating C++ code

%prep
%setup -q
%patch0 -p1

%build
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc README AUTHORS COPYING NEWS TODO ChangeLog
%doc examples
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*

%changelog
* Thu Dec 03 2009 Daniel Novotny <dnovotny@redhat.com> 2.0.16-5
- fixed "Source:" URL in spec (merge review: #225851)

* Mon Nov 30 2009 Daniel Novotny <dnovotny@redhat.com> 2.0.16-4
- fix #519108 class and enum names convert incorrectly in mock / koji.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Daniel Novotny <dnovotny@redhat.com> 2.0.16-1
- new upstream version 2.0.16

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Daniel Novotny <dnovotny@redhat.com> - 2.0.15-3
- summary fix

* Wed Feb 13 2008 Tomas Smetana <tsmetana@redhat.com> - 2.0.15-2
- rebuild (gcc-4.3)

* Mon Dec 03 2007 Tomas Smetana <tsmetana@redhat.com> - 2.0.15-1
- new upstream version

* Wed Aug 29 2007 Tomas Smetana <tsmetana@redhat.com> - 2.0.14-4
- rebuild (because of BuildID)

* Mon Aug 20 2007 Tomas Smetana <tsmetana@redhat.com> - 2.0.14-3
- license tag update

* Wed Apr 18 2007 Harald Hoyer <harald@redhat.com> - 2.0.14-2
- specfile review

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.14-1.1
- rebuild

* Mon May 29 2006 Harald Hoyer <harald@redhat.com> - 2.0.14-1
- more build requires (bug #193395)
- new version 2.0.14

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.0.12-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.0.12-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 16 2005 Harald Hoyer <harald@redhat.com>
- version 2.0.12

* Wed Mar 02 2005 Harald Hoyer <harald@redhat.com> 
- rebuilt

* Wed Feb 09 2005 Harald Hoyer <harald@redhat.com>
- rebuilt

* Mon Nov 22 2004 Harald Hoyer <harald@faro.stuttgart.redhat.com> - 2.0.11-1
- version 2.0.11

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 29 2004 Harald Hoyer <harald@faro.stuttgart.redhat.com> - 2.0.6-3
- BuildRequires glib2-devel (111009)

* Wed Aug  6 2003 Harald Hoyer <harald@redhat.de> 2.0.6-2
- rebuild, redhatified specfile

* Fri Sep 28 2001  George Lebl <jirka@5z.com>
- Updated for gob2

* Tue Feb 7 2000  George Lebl <jirka@5z.com>
- added %%{prefix}/share/aclocal/* to %%files

* Tue Dec 14 1999  George Lebl <jirka@5z.com>
- added the examples dir to the %%doc

* Mon Aug 16 1999  George Lebl <jirka@5z.com>
- added gob.spec.in file

